import Function as f;

function MoveLoc(Unit : TrgUnit, cp : TrgPlayer, x, y);
function SkillUnit(cp : TrgPlayer, count, Unit : TrgUnit);
function SquareShapeAt(cp : TrgPlayer, count, Unit : TrgUnit, x, y, distanceX, distanceY);
function NxNSquareShapeAt(cp : TrgPlayer, count, Unit : TrgUnit, n, interval, distanceX, distanceY);

var i = 0;

function main(cp)
{
   MoveLocation("26.Yume_Bozo", f.heroID[cp], cp, "Anywhere");

   if (cp < 3)
   {
      if (Bring(3, AtLeast, 1, f.heroID[3], "26.Yume_Bozo"))
      {
         KillUnitAt(All, "Protoss Observer", "Anywhere", 3);
      }
      if (Bring(4, AtLeast, 1, f.heroID[4], "26.Yume_Bozo"))
      {
         KillUnitAt(All, "Protoss Observer", "Anywhere", 4);
      }
      if (Bring(5, AtLeast, 1, f.heroID[5], "26.Yume_Bozo"))
      {
         KillUnitAt(All, "Protoss Observer", "Anywhere", 5);
      }
   }
   else if (cp >= 3)
   {
      if (Bring(0, AtLeast, 1, f.heroID[0], "26.Yume_Bozo"))
      {
         KillUnitAt(All, "Protoss Observer", "Anywhere", 0);
      }
      if (Bring(1, AtLeast, 1, f.heroID[1], "26.Yume_Bozo"))
      {
         KillUnitAt(All, "Protoss Observer", "Anywhere", 1);
      }
      if (Bring(2, AtLeast, 1, f.heroID[2], "26.Yume_Bozo"))
      {
         KillUnitAt(All, "Protoss Observer", "Anywhere", 2);
      }
   }

   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {             
            SetSwitch("ComputerAlliy", Set);

            SetAllianceStatus(P7, Ally);
            SetAllianceStatus(P8, Ally);

            f.DotShape(cp, 1, "40 + 1n Gantrithor", 0, 0);
            KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);

            SetInvincibility(Enable, f.heroID[cp], cp, "Anywhere");

            f.SkillWait(cp, 560);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {
            MoveLocation("26.Yume_Bozo", f.heroID[cp], cp, "Anywhere");

            i = 0;

            if (cp < 3)
            {
               if (Bring(3, AtLeast, 1, f.heroID[3], "26.Yume_Bozo"))
               {
                  CreateUnitWithProperties(1, "Zerg Defiler", "[Skill]Unit_Wait_1", cp, UnitProperty(burrowed=True));
                  SetInvincibility(Enable, "Any unit", cp, "[Skill]Unit_Wait_ALL");
                  MoveLocation(f.location[cp], f.heroID[3], 3, "Anywhere");
                  MoveUnit(All, "Zerg Defiler", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);

                  i += 1;
               }
               if (Bring(4, AtLeast, 1, f.heroID[4], "26.Yume_Bozo"))
               {
                  CreateUnitWithProperties(1, "Zerg Defiler", "[Skill]Unit_Wait_1", cp, UnitProperty(burrowed=True));
                  SetInvincibility(Enable, "Any unit", cp, "[Skill]Unit_Wait_ALL");
                  MoveLocation(f.location[cp], f.heroID[4], 4, "Anywhere");
                  MoveUnit(All, "Zerg Defiler", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);

                  i += 1;
               }
               if (Bring(5, AtLeast, 1, f.heroID[5], "26.Yume_Bozo"))
               {
                  CreateUnitWithProperties(1, "Zerg Defiler", "[Skill]Unit_Wait_1", cp, UnitProperty(burrowed=True));
                  SetInvincibility(Enable, "Any unit", cp, "[Skill]Unit_Wait_ALL");
                  MoveLocation(f.location[cp], f.heroID[5], 5, "Anywhere");
                  MoveUnit(All, "Zerg Defiler", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);

                  i += 1;
               }

            }
            else if (cp >= 3)
            {
               if (Bring(0, AtLeast, 1, f.heroID[0], "26.Yume_Bozo"))
               {
                  CreateUnitWithProperties(1, "Zerg Defiler", "[Skill]Unit_Wait_1", cp, UnitProperty(burrowed=True));
                  SetInvincibility(Enable, "Any unit", cp, "[Skill]Unit_Wait_ALL");
                  MoveLocation(f.location[cp], f.heroID[0], 0, "Anywhere");
                  MoveUnit(All, "Zerg Defiler", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);

                  i += 1;                  
               }
               if (Bring(1, AtLeast, 1, f.heroID[1], "26.Yume_Bozo"))
               {
                  CreateUnitWithProperties(1, "Zerg Defiler", "[Skill]Unit_Wait_1", cp, UnitProperty(burrowed=True));
                  SetInvincibility(Enable, "Any unit", cp, "[Skill]Unit_Wait_ALL");
                  MoveLocation(f.location[cp], f.heroID[1], 1, "Anywhere");
                  MoveUnit(All, "Zerg Defiler", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);

                  i += 1;                  
               }
               if (Bring(2, AtLeast, 1, f.heroID[2], "26.Yume_Bozo"))
               {
                  CreateUnitWithProperties(1, "Zerg Defiler", "[Skill]Unit_Wait_1", cp, UnitProperty(burrowed=True));
                  SetInvincibility(Enable, "Any unit", cp, "[Skill]Unit_Wait_ALL");
                  MoveLocation(f.location[cp], f.heroID[2], 2, "Anywhere");
                  MoveUnit(All, "Zerg Defiler", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);

                  i += 1;                  
               }
            }

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] < 4)
         {        
            RemoveUnitAt(All, "80 + 1n Artanis", "Anywhere", cp);
            RemoveUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", cp);

            var j = 0;    

            for (; j < i; j++)
            {
               if (f.loop[cp] == 0)
               {
                  f.Table_Sin(cp, 22, 100);
                  f.Table_Cos(cp, 22, 100);

                  var x = f.CosAngle[cp];
                  var y = f.SinAngle[cp];

                  NxNSquareShapeAt(cp, 1, "80 + 1n Artanis", 4, 50, x, y);
                  NxNSquareShapeAt(cp, 1, "80 + 1n Artanis", 4, 50, -x, -y);
                  NxNSquareShapeAt(cp, 1, "80 + 1n Artanis", 4, 50, -y, x);
                  NxNSquareShapeAt(cp, 1, "80 + 1n Artanis", 4, 50, y, -x);
                  NxNSquareShapeAt(cp, 1, " Unit. Hoffnung 25000", 4, 50, x, y);
                  NxNSquareShapeAt(cp, 1, " Unit. Hoffnung 25000", 4, 50, -x, -y);
                  NxNSquareShapeAt(cp, 1, " Unit. Hoffnung 25000", 4, 50, -y, x);
                  NxNSquareShapeAt(cp, 1, " Unit. Hoffnung 25000", 4, 50, y, -x);
               }
               else if (f.loop[cp] == 1)
               {
                  f.Table_Sin(cp, 22, 100);
                  f.Table_Cos(cp, 22, 100);

                  var x = f.CosAngle[cp];
                  var y = f.SinAngle[cp];

                  NxNSquareShapeAt(cp, 1, "Kakaru (Twilight)", 4, 50, x, y);
                  NxNSquareShapeAt(cp, 1, "Kakaru (Twilight)", 4, 50, -x, -y);
                  NxNSquareShapeAt(cp, 1, "Kakaru (Twilight)", 4, 50, -y, x);
                  NxNSquareShapeAt(cp, 1, "Kakaru (Twilight)", 4, 50, y, -x);
               }
               else if (f.loop[cp] == 2)
               {
                  f.Table_Sin(cp, 67, 100);
                  f.Table_Cos(cp, 67, 100);

                  var x = f.CosAngle[cp];
                  var y = f.SinAngle[cp];

                  NxNSquareShapeAt(cp, 1, "80 + 1n Tom Kazansky", 4, 50, x, y);
                  NxNSquareShapeAt(cp, 1, "80 + 1n Tom Kazansky", 4, 50, -x, -y);
                  NxNSquareShapeAt(cp, 1, "80 + 1n Tom Kazansky", 4, 50, -y, x);
                  NxNSquareShapeAt(cp, 1, "80 + 1n Tom Kazansky", 4, 50, y, -x);
                  NxNSquareShapeAt(cp, 1, " Unit. Hoffnung 25000", 4, 50, x, y);
                  NxNSquareShapeAt(cp, 1, " Unit. Hoffnung 25000", 4, 50, -x, -y);
                  NxNSquareShapeAt(cp, 1, " Unit. Hoffnung 25000", 4, 50, -y, x);
                  NxNSquareShapeAt(cp, 1, " Unit. Hoffnung 25000", 4, 50, y, -x);
               }
               else if (f.loop[cp] == 3)
               {
                  f.Table_Sin(cp, 67, 100);
                  f.Table_Cos(cp, 67, 100);

                  var x = f.CosAngle[cp];
                  var y = f.SinAngle[cp];

                  NxNSquareShapeAt(cp, 1, "Kakaru (Twilight)", 4, 50, x, y);
                  NxNSquareShapeAt(cp, 1, "Kakaru (Twilight)", 4, 50, -x, -y);
                  NxNSquareShapeAt(cp, 1, "Kakaru (Twilight)", 4, 50, -y, x);
                  NxNSquareShapeAt(cp, 1, "Kakaru (Twilight)", 4, 50, y, -x);
               }

               CreateUnitWithProperties(1, "40 + 1n Zergling", "[Skill]Unit_Wait_1", cp, UnitProperty(burrowed=True));
               SetInvincibility(Enable, "Any unit", cp, "[Skill]Unit_Wait_ALL");
               MoveLocation(f.location[cp], "Zerg Defiler", cp, "Anywhere");
               RemoveUnitAt(1, "Zerg Defiler", "Anywhere", cp);
               MoveUnit(All, "40 + 1n Zergling", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);

            }

            Order("80 + 1n Artanis", cp, "Anywhere", Attack, "Anywhere");
            Order("80 + 1n Tom Kazansky", cp, "Anywhere", Attack, "Anywhere");

            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            j = 0;

            for (; j < i; j++)
            {
               CreateUnitWithProperties(1, "Zerg Defiler", "[Skill]Unit_Wait_1", cp, UnitProperty(burrowed=True));
               SetInvincibility(Enable, "Any unit", cp, "[Skill]Unit_Wait_ALL");
               MoveLocation(f.location[cp], "40 + 1n Zergling", cp, "Anywhere");
               RemoveUnitAt(1, "40 + 1n Zergling", "Anywhere", cp);
               MoveUnit(All, "Zerg Defiler", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            }

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {
            RemoveUnitAt(All, "80 + 1n Artanis", "Anywhere", cp);
            RemoveUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", cp);
            RemoveUnitAt(All, "Zerg Defiler", "Anywhere", cp);

            f.SkillWait(cp, 2320);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 2)
      {
         if (f.loop[cp] == 0)
         {         
            f.DotShape(cp, 1, "40 + 1n Gantrithor", 0, 0);
            KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);

            SetInvincibility(Disable, f.heroID[cp], cp, "Anywhere");

            f.SkillWait(cp, 480);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {         
            f.Voice_Routine(cp, 6);

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 3)
      {
         SetSwitch("ComputerAlliy", Clear);

         if (cp < 3)
         {
            SetAllianceStatus(P8, Enemy);
         }
         else if (cp >= 3)
         {
            SetAllianceStatus(P7, Enemy);
         }

         f.SkillEnd(cp);
      }
   }
}



function MoveLoc(Unit : TrgUnit, cp : TrgPlayer, x, y)
{
   MoveLocation(f.location[cp], "Zerg Defiler", cp, "Anywhere");
   addloc(f.location[cp], x, y);
}

function SkillUnit(cp : TrgPlayer, count, Unit : TrgUnit)
{
   CreateUnit(count, Unit, dwrand() % 8 + 33, cp);
   SetInvincibility(Enable, Unit, cp, "[Skill]Unit_Wait_ALL");
   MoveUnit(count, Unit, cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
}

function SquareShapeAt(cp : TrgPlayer, count, Unit : TrgUnit, x, y, distanceX, distanceY)
{
   MoveLoc(f.heroID[cp], cp, x + distanceX, y + distanceY);
   SkillUnit(cp, count, Unit);
   MoveLoc(f.heroID[cp], cp, -y + distanceX, x + distanceY);
   SkillUnit(cp, count, Unit);
   MoveLoc(f.heroID[cp], cp, -x + distanceX, -y + distanceY);
   SkillUnit(cp, count, Unit);
   MoveLoc(f.heroID[cp], cp, y + distanceX, -x + distanceY);
   SkillUnit(cp, count, Unit);
}

function NxNSquareShapeAt(cp : TrgPlayer, count, Unit : TrgUnit, n, interval, distanceX, distanceY)
{
   var i = 0;
   var destX, destY; 
   var distance = interval / 2;
   var size = n * n;
   
   for (; i < size / 4; i++)
   {
      if (n == 1)
      {
         MoveLoc(f.heroID[cp] ,cp, distanceX, distanceY);
         SkillUnit(cp, count, Unit);
      }
      else if (n % 2 == 0)
      {
         destX = i % (n / 2) + 1;
         destY = i / (n / 2) + 1;
         
         if (destX == 1)
         {
            SquareShapeAt(cp, count, Unit, distance, destY * interval - distance, distanceX, distanceY);
         }
         else if (destY == 1)
         {
            SquareShapeAt(cp, count, Unit, destX * interval - distance, distance, distanceX, distanceY);
         }
         else
         {
            SquareShapeAt(cp, count, Unit, destX * interval - distance, destY * interval - distance, distanceX, distanceY);
         }
      }
      else if (n % 2 == 1)
      {
         destX = i % (n / 2);
         destY = i / (n / 2);
   
         if (i == 0)
         {
            MoveLoc(f.heroID[cp] ,cp, distanceX, distanceY);
            SkillUnit(cp, count, Unit);
         }
         else if (destY == 0)
         {
            SquareShapeAt(cp, count, Unit, destX * interval, 0, distanceX, distanceY);
         }
         else
         {
            SquareShapeAt(cp, count, Unit, destX * interval + interval, destY * interval, distanceX, distanceY);
         }
         
         if (i == size / 4 - 1)
         {
            SquareShapeAt(cp, count, Unit, (n / 2) * interval, 0, distanceX, distanceY);
         }
      }
   }
}