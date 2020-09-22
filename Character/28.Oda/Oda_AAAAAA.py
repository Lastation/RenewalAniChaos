import Function as f;

var v = 0;

function main(cp)
{
   f.HoldPosition(cp);
   f.BanReturn(cp);

   MoveUnit(All, " Unit. Schnee", cp, "Anywhere", "[Skill]HoldPosition");

   if (v != 0)
      f.Voice_Routine(cp, 7 + v);

   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 8)
         {
            v = 1;

            f.DotShape(cp, 1, "60 + 1n Danimoth", 200, 0);
            KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", cp);
            f.DotShape(cp, 1, " Unit. Schnee", 200, 0);
         }
         if (f.loop[cp] == 28)
         {
            v = 2;
         }

         f.SkillWait(cp, 160);

         f.loop[cp] += 1;

         if (f.loop[cp] == 65)
         {
            v = 3;

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] == 0)
         {
            SetSwitch("Recall - Oda", Set);
         }
         else if (f.loop[cp] == 1)
         {
            KillUnitAt(All, " Unit. Schnee", "Anywhere", cp);
         }

         f.SkillWait(cp, 160);

         f.loop[cp] += 1;

         if (f.loop[cp] == 30)
         {
            v = 4;

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 2)
      {
         if (f.loop[cp] < 5)
         {
            f.EdgeShape(cp, 1, " Unit. Hoffnung 25000", 45, 3 + 2 * f.loop[cp], 75 * (f.loop[cp] + 1));
         }
         KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

         if (f.loop[cp] == 5)
         {
            f.NxNSquareShape(cp, 1, " Unit. Hoffnung 25000", 11, 75);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            var i = 0;

            for (; i < 5; i++)
            {
               f.EdgeShapeBurrowed(cp, 1, "40 + 1n Lurker", 45, 3 + i, 75 + 75 * i);
            }

            v = 5;

         }
         if (f.loop[cp] == 15)
         {
            v = 5;
         }

         f.SkillWait(cp, 160);

         f.loop[cp] += 1;

         if (f.loop[cp] == 36)
         {
            v = 0;

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 3)
      {


         f.EdgeShape(cp, 1, " Unit. Hoffnung 25000", 45, 3, 50);
         KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

         f.SkillWait(cp, 160);

         f.loop[cp] += 1;

         if (f.loop[cp] == 26)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 4)
      {
         if (f.loop[cp] == 0)
         {
            f.NxNSquareShape(cp, 1, "40 + 1n Wraith", 6, 50);
            f.NxNSquareShape(cp, 1, " Unit. Hoffnung 25000", 6, 50);
         }
         else if (f.loop[cp] == 2)
         {
            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.NxNSquareShape(cp, 1, "40 + 1n Wraith", 11, 50);
            f.NxNSquareShape(cp, 1, " Unit. Hoffnung 25000", 11, 50);
         }
         else if (f.loop[cp] == 4)
         {
            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.NxNSquareShape(cp, 1, "50 + 1n Battlecruiser", 11, 75);
            f.NxNSquareShape(cp, 1, " Unit. Hoffnung 25000", 11, 75);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, f.location[cp]);
         }

         MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
         Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);

         KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

         f.SkillWait(cp, 160);

         f.loop[cp] += 1;

         if (f.loop[cp] == 8)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 5)
      {
         CreateUnit(16, "80 + 1n Guardian", dwrand() % 8 + 33, cp);
         CreateUnit(4, "40 + 1n Guardian", dwrand() % 8 + 33, cp);
         SetInvincibility(Enable, "Any unit", cp, "[Skill]Unit_Wait_ALL");

         var i = 0;

         for (; i < 4; i++)
         {
            if (Bring(cp, AtLeast, 1, "50 + 1n Battlecruiser", "Anywhere"))
            {
               var x = dwrand() % 20 + 10;

               MoveLocation(f.location[cp], "50 + 1n Battlecruiser", cp, "Anywhere");
               RemoveUnitAt(1, "50 + 1n Battlecruiser", "Anywhere", cp);
               MoveUnit(1, "40 + 1n Guardian", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
               addloc(f.location[cp], x, x);
               MoveUnit(1, "80 + 1n Guardian", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
               addloc(f.location[cp], -x, -x);
               MoveUnit(1, "80 + 1n Guardian", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
               addloc(f.location[cp], -x, x);
               MoveUnit(1, "80 + 1n Guardian", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
               addloc(f.location[cp], x, -x);
               MoveUnit(1, "80 + 1n Guardian", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            }
         }

         MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
         Order("40 + 1n Guardian", cp, "Anywhere", Attack, f.location[cp]);

         KillUnitAt(All, "80 + 1n Guardian", "Anywhere", cp);

         f.SkillWait(cp, 160);

         f.loop[cp] += 1;

         if (f.loop[cp] == 32)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 6)
      {
         if (f.loop[cp] % 3 == 0)
         {
            f.Table_Sin(cp, 0, 40 * (f.loop[cp] / 3));
            f.Table_Cos(cp, 0, 40 * (f.loop[cp] / 3));

            var x = f.CosAngle[cp];
            var y = f.SinAngle[cp];

            f.NxNSquareShapeAt(cp, 1, "40 + 1n Wraith", 2, 50, x, y);
            f.NxNSquareShapeAt(cp, 1, "40 + 1n Wraith", 2, 50, -x, -y);
            f.NxNSquareShapeAt(cp, 1, "40 + 1n Wraith", 2, 50, -y, x);
            f.NxNSquareShapeAt(cp, 1, "40 + 1n Wraith", 2, 50, y, -x);

            f.NxNSquareShapeAt(cp, 1, " Unit. Hoffnung 25000", 2, 50, x, y);
            f.NxNSquareShapeAt(cp, 1, " Unit. Hoffnung 25000", 2, 50, -x, -y);
            f.NxNSquareShapeAt(cp, 1, " Unit. Hoffnung 25000", 2, 50, -y, x);
            f.NxNSquareShapeAt(cp, 1, " Unit. Hoffnung 25000", 2, 50, y, -x);
         }
         else if (f.loop[cp] % 3 == 1)
         {
            f.Table_Sin(cp, 30, 40 * (f.loop[cp] / 3));
            f.Table_Cos(cp, 30, 40 * (f.loop[cp] / 3));

            var x = f.CosAngle[cp];
            var y = f.SinAngle[cp];

            f.NxNSquareShapeAt(cp, 1, "40 + 1n Mojo", 2, 50, x, y);
            f.NxNSquareShapeAt(cp, 1, "40 + 1n Mojo", 2, 50, -x, -y);
            f.NxNSquareShapeAt(cp, 1, "40 + 1n Mojo", 2, 50, -y, x);
            f.NxNSquareShapeAt(cp, 1, "40 + 1n Mojo", 2, 50, y, -x);

            f.NxNSquareShapeAt(cp, 1, " Unit. Hoffnung 25000", 2, 50, x, y);
            f.NxNSquareShapeAt(cp, 1, " Unit. Hoffnung 25000", 2, 50, -x, -y);
            f.NxNSquareShapeAt(cp, 1, " Unit. Hoffnung 25000", 2, 50, -y, x);
            f.NxNSquareShapeAt(cp, 1, " Unit. Hoffnung 25000", 2, 50, y, -x);
         }
         else if (f.loop[cp] % 3 == 2)
         {
            f.Table_Sin(cp, 60, 40 * (f.loop[cp] / 3));
            f.Table_Cos(cp, 60, 40 * (f.loop[cp] / 3));

            var x = f.CosAngle[cp];
            var y = f.SinAngle[cp];

            f.NxNSquareShapeAt(cp, 1, "40 + 1n Mutalisk", 2, 50, x, y);
            f.NxNSquareShapeAt(cp, 1, "40 + 1n Mutalisk", 2, 50, -x, -y);
            f.NxNSquareShapeAt(cp, 1, "40 + 1n Mutalisk", 2, 50, -y, x);
            f.NxNSquareShapeAt(cp, 1, "40 + 1n Mutalisk", 2, 50, y, -x);

            f.NxNSquareShapeAt(cp, 1, " Unit. Hoffnung 25000", 2, 50, x, y);
            f.NxNSquareShapeAt(cp, 1, " Unit. Hoffnung 25000", 2, 50, -x, -y);
            f.NxNSquareShapeAt(cp, 1, " Unit. Hoffnung 25000", 2, 50, -y, x);
            f.NxNSquareShapeAt(cp, 1, " Unit. Hoffnung 25000", 2, 50, y, -x);
         }

         MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
         Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);
         Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);
         Order("40 + 1n Mutalisk", cp, "Anywhere", Attack, f.location[cp]);

         KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 32)
         {
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 7)
      {
         f.SkillWait(cp, 3200);

         f.count[cp] += 1;
         f.loop[cp] = 0;  
      }
      else if (f.count[cp] == 8)
      {
         KillUnitAt(All, "40 + 1n Lurker", "Anywhere", cp);
         KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);
         KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
         KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

         SetSwitch("UiltimateSwitch", Clear);
         SetSwitch("Recall - Oda", Clear);

         f.SkillEnd(cp);
      }
   }

   MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
}