import Function as f;

var v = 0;

function main(cp)
{
   if (f.count[cp] >= 3)
   {
      f.HoldPosition(cp);
   }

   f.BanReturn(cp);

   MoveUnit(All, " Unit. Schnee", cp, "Anywhere", "[Skill]HoldPosition");

   ModifyUnitShields(All, f.heroID[cp], cp, "Anywhere", 1);

   if (v != 0)
      f.Voice_Routine(cp, 7 + v);

   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {
            v = 3;

            SetDeaths(cp, SetTo, 1, " `ShieldRecharge");            
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
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] == 0)
         {
            SetSwitch("Recall - Oda", Set);
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
      else if (f.count[cp] == 2)
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
      else if (f.count[cp] == 3)
      {
         if (f.loop[cp] == 0)
         {
            f.NxNSquareShape(cp, 1, "40 + 1n Guardian", 6, 50);
         }
         else if (f.loop[cp] == 2)
         {
            f.NxNSquareShape(cp, 1, "40 + 1n Guardian", 11, 50);
         }
         else if (f.loop[cp] == 4)
         {
            f.NxNSquareShape(cp, 1, "40 + 1n Wraith", 11, 75);
            f.NxNSquareShape(cp, 1, " Unit. Hoffnung 25000", 11, 75);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);
         }
         else if (f.loop[cp] == 6)
         {
            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.NxNSquareShape(cp, 1, "50 + 1n Battlecruiser", 11, 75);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, f.location[cp]);
         }

         KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
         KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

         f.SkillWait(cp, 160);

         f.loop[cp] += 1;

         if (f.loop[cp] == 8)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 4)
      {
         CreateUnit(24, "80 + 1n Guardian", dwrand() % 8 + 33, cp);
         CreateUnit(6, "40 + 1n Guardian", dwrand() % 8 + 33, cp);
         SetInvincibility(Enable, "Any unit", cp, "[Skill]Unit_Wait_ALL");

         var i = 0;

         for (; i < 6; i++)
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

         if (f.loop[cp] == 25)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 5)
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
      else if (f.count[cp] == 6)
      {
         f.SkillWait(cp, 3200);

         f.count[cp] += 1;
         f.loop[cp] = 0;  
      }
      else if (f.count[cp] == 7)
      {
         KillUnitAt(All, "40 + 1n Lurker", "Anywhere", cp);
         KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);
         KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
         KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

         SetSwitch("UiltimateSwitch", Clear);
         SetSwitch("Recall - Oda", Clear);
         SetDeaths(cp, SetTo, 0, " `ShieldRecharge");

         f.SkillEnd(cp);
      }
   }

   MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
}