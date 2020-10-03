import Function as f;

function EdgeShapeAt(cp : TrgPlayer, count, Unit : TrgUnit, degree, n, interval, x, y);

function main(cp)
{
   MoveUnit(All, "50 + 1n Battlecruiser", cp, "Anywhere", "[Skill]HoldPosition");
   MoveUnit(All, "40 + 1n Gantrithor", cp, "Anywhere", "[Skill]HoldPosition");

   f.BanReturn(cp);
   f.HoldPosition(cp);

   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         f.Table_Sin(cp, 22 * f.loop[cp], 150);
         f.Table_Cos(cp, 22 * f.loop[cp], 150);

         var x = f.CosAngle[cp];
         var y = f.SinAngle[cp];

         f.SquareShape(cp, 1, "40 + 1n Lurker", x, y);
         KillUnitAt(All, "40 + 1n Lurker", "Anywhere", cp);

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 4)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 1)
      {
         RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

         f.Table_Sin(cp, 45 * f.loop[cp], 100);
         f.Table_Cos(cp, 45 * f.loop[cp], 100);

         var x = f.CosAngle[cp];
         var y = f.SinAngle[cp];

         f.DoubleShape(cp, 1, "40 + 1n Wraith", x, y);
         f.DoubleShape(cp, 1, "Scantid (Desert)", x, y);
         KillUnitAt(All, "Scantid (Desert)", "Anywhere", cp);

         MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
         Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 4)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 2)
      {
         f.Table_Sin(cp, 90 - 22 * f.loop[cp], 150);
         f.Table_Cos(cp, 90 - 22 * f.loop[cp], 150);

         var x = f.CosAngle[cp];
         var y = f.SinAngle[cp];

         if (f.loop[cp] % 2 == 0)
         {
            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            if (f.loop[cp] == 0)
            {
               f.SquareShape(cp, 1, "50 + 1n Battlecruiser", x, y);
            }
            else if (f.loop[cp] == 2)
            {
               f.SquareShape(cp, 1, "100 + 1n Hyperion", x, y);
            }
            f.SquareShape(cp, 1, "50 + 1n Tank", x, y);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("100 + 1n Hyperion", cp, "Anywhere", Attack, f.location[cp]);
            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, f.location[cp]);
         }
         else if (f.loop[cp] % 2 == 1)
         {
            f.SquareShape(cp, 1, "40 + 1n Gantrithor", x, y);
            f.SquareShape(cp, 1, "60 + 1n Archon", x, y);
            KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 4)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 3)
      {
         if (f.loop[cp] < 4)
         {
            var x = 300 - 75 * f.loop[cp];
            var y = 75 * f.loop[cp];

            f.SquareShape(cp, 1, "60 + 1n Siege", x, y);
            f.SquareShape(cp, 8, "Protoss Dark Archon", x, y);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            if (f.loop[cp] == 0)
            {
               KillUnitAt(All, "100 + 1n Hyperion", "Anywhere", cp);

               f.Table_Sin(cp, 90, 150);
               f.Table_Cos(cp, 90, 150);

               x = f.CosAngle[cp];
               y = f.SinAngle[cp];

               f.SquareShape(cp, 9, "60 + 1n Archon", x, y);
               KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            }
            else if (f.loop[cp] == 2)
            {
               f.Table_Sin(cp, 45, 150);
               f.Table_Cos(cp, 45, 150);

               x = f.CosAngle[cp];
               y = f.SinAngle[cp];

               f.SquareShape(cp, 1, "40 + 1n Gantrithor", x, y);
               f.SquareShape(cp, 9, "60 + 1n Archon", x, y);
               KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
            }
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 4)
         {
            ModifyUnitHangarCount(2, All, "40 + 1n Gantrithor", CurrentPlayer, "Anywhere");
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Gantrithor", cp, "Anywhere", Attack, f.location[cp]);

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 4)
      {
         var x = 0;
         var y = 0;

         if (f.loop[cp] < 4)
         {
            var i = 0;

            for (; i <= f.loop[cp]; i++)
            {
               f.Table_Sin(cp, 22 + 45 * i, 50 + 75 * i);
               f.Table_Cos(cp, 22 + 45 * i, 50 + 75 * i);

               x = f.CosAngle[cp];
               y = f.SinAngle[cp];

               EdgeShapeAt(cp, 1, "60 + 1n High Templar", 22, 3, 32, x, y);
               KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);
            }
         }

         var r = 0;
         var d = 0;

         if (f.loop[cp] == 3)
         {
            r = 22;
            d = 200;
         }
         else if (f.loop[cp] == 4)
         {
            r = 67;
            d = 150;
         }
         else if (f.loop[cp] == 5)
         {
            r = 22;
            d = 250;
         }
         else if (f.loop[cp] == 6)
         {
            r = 67;
            d = 100;
         }
         else if (f.loop[cp] == 7)
         {
            r = 67;
            d = 250;

            SetSwitch("Recall - Oda", Set);
         }
         KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

         if (f.loop[cp] >= 3 && f.loop[cp] < 8)
         {
            f.Table_Sin(cp, r, d);
            f.Table_Cos(cp, r, d);

            x = f.CosAngle[cp];
            y = f.SinAngle[cp];

            EdgeShapeAt(cp, 1, "40 + 1n Mojo", 22, 3, 32, x, y);
            EdgeShapeAt(cp, 1, " Unit. Hoffnung 25000", 22, 3, 32, x, y);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            f.Table_Sin(cp, r + 90, d);
            f.Table_Cos(cp, r + 90, d);

            x = f.CosAngle[cp];
            y = f.SinAngle[cp];

            EdgeShapeAt(cp, 1, "Target", 22, 3, 32, x, y);
            EdgeShapeAt(cp, 1, "60 + 1n Archon", 22, 3, 32, x, y);
            KillUnitAt(All, "Target", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            if (f.loop[cp] % 2 == 1)
            {
               MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
               Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);
            }

            if (f.loop[cp] == 3)
            {
               f.DotShape(cp, 1, "40 + 1n Goliath", x, y);
               f.DotShape(cp, 1, "40 + 1n Goliath", -x, -y);
               f.DotShape(cp, 1, "40 + 1n Goliath", -y, x);
               f.DotShape(cp, 1, "40 + 1n Goliath", y, -x);

               MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
               MoveUnit(All, "40 + 1n Goliath", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
               Order("40 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]);
            }
            if (f.loop[cp] == 4)
            {
               f.DotShape(cp, 1, "40 + 1n Drone", x, y);
               f.DotShape(cp, 1, "40 + 1n Drone", -x, -y);
               f.DotShape(cp, 1, "40 + 1n Drone", -y, x);
               f.DotShape(cp, 1, "40 + 1n Drone", y, -x);

               MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
               MoveUnit(All, "40 + 1n Drone", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
               Order("40 + 1n Drone", cp, "Anywhere", Attack, f.location[cp]);
            }
            if (f.loop[cp] == 5)
            {
               f.DotShape(cp, 1, "50 + 1n Tank", x, y);
               f.DotShape(cp, 1, "50 + 1n Tank", -x, -y);
               f.DotShape(cp, 1, "50 + 1n Tank", -y, x);
               f.DotShape(cp, 1, "50 + 1n Tank", y, -x);

               MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
               MoveUnit(All, "50 + 1n Tank", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
               Order("50 + 1n Tank", cp, "Anywhere", Attack, f.location[cp]);
            }
            if (f.loop[cp] == 6)
            {
               f.DotShape(cp, 1, "40 + 1n Drone", x, y);
               f.DotShape(cp, 1, "40 + 1n Drone", -x, -y);
               f.DotShape(cp, 1, "40 + 1n Drone", -y, x);
               f.DotShape(cp, 1, "40 + 1n Drone", y, -x);

               MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
               MoveUnit(All, "40 + 1n Drone", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
               Order("40 + 1n Drone", cp, "Anywhere", Attack, f.location[cp]);
            }
            if (f.loop[cp] == 7)
            {
               f.DotShape(cp, 1, "60 + 1n Dragoon", x, y);
               f.DotShape(cp, 1, "60 + 1n Dragoon", -x, -y);
               f.DotShape(cp, 1, "60 + 1n Dragoon", -y, x);
               f.DotShape(cp, 1, "60 + 1n Dragoon", y, -x);

               MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
               MoveUnit(All, "60 + 1n Dragoon", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
               Order("60 + 1n Dragoon", cp, "Anywhere", Attack, f.location[cp]);
            }

         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 67)
         {
            f.Voice_Routine(cp, 23);

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 5)
      {
         if (f.loop[cp] == 0)
         {
            KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);

         }
         if (f.loop[cp] == 18)
         {
            KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Drone", "Anywhere", cp);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Siege", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", cp);

            SetSwitch("Recall - Oda", Clear);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 19)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 6)
      {
         f.SkillEnd(cp);
      }
   }

   MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
}

function EdgeShapeAt(cp : TrgPlayer, count, Unit : TrgUnit, degree, n, interval, x, y)
{
   f.EdgeShapeAt(cp, count, Unit, degree, n, interval, x, y);
   f.EdgeShapeAt(cp, count, Unit, degree, n, interval, -x, -y);
   f.EdgeShapeAt(cp, count, Unit, degree, n, interval, -y, x);
   f.EdgeShapeAt(cp, count, Unit, degree, n, interval, y, -x);

   f.DotShape(cp, count, Unit, x, y);
   f.DotShape(cp, count, Unit, -x, -y);
   f.DotShape(cp, count, Unit, -y, x);
   f.DotShape(cp, count, Unit, y, -x);
}

