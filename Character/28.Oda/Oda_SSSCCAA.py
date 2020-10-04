import Function as f;

function main(cp)
{
   MoveUnit(All, "50 + 1n Tank", cp, "Anywhere", "[Skill]HoldPosition");
   MoveUnit(All, "60 + 1n Dragoon", cp, "Anywhere", "[Skill]HoldPosition");
   MoveUnit(All, "40 + 1n Drone", cp, "Anywhere", "[Skill]HoldPosition");

   f.BanReturn(cp);
   f.HoldPosition(cp);

   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {
            f.Table_Sin(cp, 22, 100);
            f.Table_Cos(cp, 22, 100);

            f.SquareShape(cp, 1, "50 + 1n Tank", f.CosAngle[cp], f.SinAngle[cp]);
            f.SquareShape(cp, 1, "40 + 1n Gantrithor", f.CosAngle[cp], f.SinAngle[cp]);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);

            f.Table_Sin(cp, 67, 150);
            f.Table_Cos(cp, 67, 150);

            f.SquareShape(cp, 1, "60 + 1n Archon", f.CosAngle[cp], f.SinAngle[cp]);
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", f.CosAngle[cp], f.SinAngle[cp]);
            f.DotShape(cp, 1, "50 + 1n Battlecruiser", 0, 0);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, "Anywhere");
         }
         else if (f.loop[cp] == 1)
         {
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
         }
         else if (f.loop[cp] == 2)
         {
            f.Table_Sin(cp, 67, 100);
            f.Table_Cos(cp, 67, 100);

            f.SquareShape(cp, 1, "50 + 1n Tank", f.CosAngle[cp], f.SinAngle[cp]);
            f.SquareShape(cp, 1, "40 + 1n Gantrithor", f.CosAngle[cp], f.SinAngle[cp]);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);

            f.Table_Sin(cp, 22, 150);
            f.Table_Cos(cp, 22, 150);

            f.SquareShape(cp, 1, "60 + 1n Archon", f.CosAngle[cp], f.SinAngle[cp]);
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", f.CosAngle[cp], f.SinAngle[cp]);
            f.DotShape(cp, 1, "50 + 1n Battlecruiser", 0, 0);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, "Anywhere");
         }
         else if (f.loop[cp] == 3)
         {
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
         }

         f.SkillWait(cp, 160);

         f.loop[cp] += 1;

         if (f.loop[cp] == 8)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] == 0)
         {
            f.SquareShape(cp, 1, "60 + 1n Siege", 150, 150);
            f.SquareShape(cp, 1, "60 + 1n Siege", 75, 150);
            f.SquareShape(cp, 1, "60 + 1n Siege", 150, 75);
         }
         else if (f.loop[cp] == 1)
         {
            f.EdgeShape(cp, 1, "60 + 1n Dragoon", 45, 3, 75);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "60 + 1n Dragoon", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("60 + 1n Dragoon", cp, "Anywhere", Attack, f.location[cp]);
         }

         if (f.loop[cp] < 8 && f.loop[cp] % 2 == 0)
         {
            var x = 150;
            var y = 50 * (f.loop[cp] / 2);

            var i = 0;

            for (; i < 4; i++)
            {
               f.SquareShape(cp, 1, "Protoss Dark Archon", x - 50 * i, y - x);
               f.SquareShape(cp, 1, "40 + 1n Mojo", x - 50 * i, y);
            }

            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);


         }

         if (f.loop[cp] == 9)
         {
            f.EdgeShape(cp, 1, "60 + 1n Danimoth", 45, 5, 100);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("60 + 1n Danimoth", cp, "Anywhere", Attack, f.location[cp]);
         }
         else if (f.loop[cp] == 13)
         {
            KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", cp);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 22)
         {
            KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", cp);

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 2)
      {
         if (f.loop[cp] == 1)
         {
            f.EdgeShape(cp, 1, "50 + 1n Tank", 45, 3, 75);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "50 + 1n Tank", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("50 + 1n Tank", cp, "Anywhere", Attack, f.location[cp]);
         }

         if (f.loop[cp] < 8 && f.loop[cp] % 2 == 0)
         {
            var x = 150;
            var y = - 50 * (f.loop[cp] / 2);

            var i = 0;

            for (; i < 4; i++)
            {
               f.SquareShape(cp, 1, "40 + 1n Wraith", x - 50 * i, y);
               f.SquareShape(cp, 1, "60 + 1n Archon", x - 50 * i, y + x);
            }

            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

         }

         if (f.loop[cp] == 9)
         {

         }
         else if (f.loop[cp] == 11)
         {
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
         }
         else if (f.loop[cp] == 12)
         {
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 0, 75);
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 0, 150);
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 225, 225);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, f.location[cp]);
         }
         else if (f.loop[cp] == 16)
         {
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 35)
         {
            f.Voice_Routine(cp, 16);

            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 3)
      {
         if (f.loop[cp] < 8 && f.loop[cp] % 2 == 0)
         {
            f.SquareShape(cp, 8, "Bengalaas (Jungle)", 160, 0);
            f.SquareShape(cp, 1, "Target", 160, 0);
            f.DotShape(cp, 1, "Target", 0, 0);

            KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", cp);
            KillUnitAt(All, "Target", "Anywhere", cp);

            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.SquareShape(cp, 1, "40 + 1n Wraith", 40 + 40 * (f.loop[cp] / 2), 0);
            f.SquareShape(cp, 1, "40 + 1n Zealot", 40 + 40 * (f.loop[cp] / 2), 0);

            f.SquareShapeWithProperty(cp, 1, "Zerg Defiler", 40 + 40 * (f.loop[cp] / 2), 0, 0);

            KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);
         }
         else if (f.loop[cp] == 8)
         {
            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.SquareShape(cp, 1, "Protoss Dark Archon", 160, 0);
            f.SquareShape(cp, 1, "Target", 160, 0);
            f.DotShape(cp, 1, "Target", 0, 0);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
            KillUnitAt(All, "Target", "Anywhere", cp);
         }
         else if (f.loop[cp] == 9)
         {
            f.SquareShape(cp, 1, "60 + 1n Archon", 160, 0);
            f.SquareShape(cp, 1, "60 + 1n Danimoth", 160, 0);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("60 + 1n Danimoth", cp, "Anywhere", Attack, f.location[cp]);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 10)
         {

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 4)
      {
         if (f.loop[cp] < 8 && f.loop[cp] % 2 == 0)
         {
            f.SquareShape(cp, 8, "Bengalaas (Jungle)", 120, 120);
            f.SquareShape(cp, 1, "Target", 120, 120);
            f.DotShape(cp, 1, "Target", 0, 0);

            KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", cp);
            KillUnitAt(All, "Target", "Anywhere", cp);

            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.SquareShape(cp, 1, "40 + 1n Wraith", 30 + 30 * (f.loop[cp] / 2), 30 + 30 * (f.loop[cp] / 2));
            f.SquareShape(cp, 1, "40 + 1n Zealot", 30 + 30 * (f.loop[cp] / 2), 30 + 30 * (f.loop[cp] / 2));

            f.SquareShapeWithProperty(cp, 1, "Zerg Defiler", 30 + 30 * (f.loop[cp] / 2), 30 + 30 * (f.loop[cp] / 2), 0);

            KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);
         }
         else if (f.loop[cp] == 8)
         {
            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.SquareShape(cp, 1, "Protoss Dark Archon", 120, 120);
            f.SquareShape(cp, 1, "Target", 120, 120);
            f.DotShape(cp, 1, "Target", 0, 0);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
            KillUnitAt(All, "Target", "Anywhere", cp);
         }
         else if (f.loop[cp] == 9)
         {
            f.SquareShape(cp, 1, "60 + 1n Archon", 120, 120);
            f.SquareShape(cp, 1, "60 + 1n Danimoth", 120, 120);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("60 + 1n Danimoth", cp, "Anywhere", Attack, f.location[cp]);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 10)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 5)
      {
         if (f.loop[cp] < 8)
         {
            var i = 0;

            for (; i < 4; i++)
            {
               CreateUnit(4, "60 + 3n Siege", dwrand() % 8 + 33, cp);
               CreateUnit(1, "40 + 1n Drone", dwrand() % 8 + 33, cp);
               SetInvincibility(Enable, "Any unit", cp, "[Skill]Unit_Wait_ALL");
               MoveLocation(f.location[cp], "Zerg Defiler", cp, "Anywhere");
               RemoveUnitAt(1, "Zerg Defiler", "Anywhere", cp);
               MoveUnit(All, "40 + 1n Drone", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
               MoveUnit(All, "60 + 3n Siege", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);

            }
            KillUnitAt(All, "60 + 3n Siege", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Drone", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Drone", cp, "Anywhere", Attack, f.location[cp]);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 31)
         {
            KillUnitAt(All, "40 + 1n Drone", "Anywhere", cp);
            f.Voice_Routine(cp, 17);
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 6)
      {
         if (f.loop[cp] < 6)
         {
            f.DoubleShape(cp, 1, "Protoss Dark Archon", 150 - 50 * f.loop[cp], 150);
            f.DoubleShape(cp, 1, "60 + 1n Archon", -150, 150 - 50 * f.loop[cp]);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
         }


         if (f.loop[cp] == 0)
         {
            KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", cp);

            f.EdgeShape(cp, 1, "60 + 1n Dragoon", 45, 3, 75);
            f.EdgeShape(cp, 1, "40 + 1n Mojo", 45, 3, 75);
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "60 + 1n Dragoon", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("60 + 1n Dragoon", cp, "Anywhere", Attack, f.location[cp]);
         }
         else if (f.loop[cp] == 2)
         {
            f.EdgeShape(cp, 1, "50 + 1n Tank", 45, 5, 150);
            f.EdgeShape(cp, 1, "40 + 1n Mojo", 45, 5, 150);
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "50 + 1n Tank", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("50 + 1n Tank", cp, "Anywhere", Attack, f.location[cp]);
         }
         else if (f.loop[cp] == 4)
         {
            f.EdgeShape(cp, 1, "Protoss Dark Archon", 22, 3, 75);
            f.EdgeShape(cp, 1, "40 + 1n Gantrithor", 22, 3, 75);
            f.DotShape(cp, 1, "40 + 1n Gantrithor", 0, 0);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);
         }
         else if (f.loop[cp] == 5)
         {
            f.EdgeShape(cp, 1, "60 + 1n Archon", 45, 3, 100);
            f.EdgeShape(cp, 1, "50 + 1n Battlecruiser", 45, 3, 100);
            f.DotShape(cp, 1, "50 + 1n Battlecruiser", 0, 0);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, "Anywhere");
         }
         else if (f.loop[cp] == 7)
         {
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
         }
         else if (f.loop[cp] == 8)
         {
            f.EdgeShape(cp, 1, "Protoss Dark Archon", 45, 3, 50);
            f.EdgeShape(cp, 1, "40 + 1n Gantrithor", 45, 3, 50);
            f.DotShape(cp, 1, "40 + 1n Gantrithor", 0, 0);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);
         }
         else if (f.loop[cp] == 9)
         {
            f.EdgeShape(cp, 1, "60 + 1n Archon", 22, 3, 75);
            f.EdgeShape(cp, 1, "50 + 1n Battlecruiser", 22, 3, 75);
            f.DotShape(cp, 1, "50 + 1n Battlecruiser", 0, 0);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, "Anywhere");
         }
         else if (f.loop[cp] == 11)
         {
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
         }
         else if (f.loop[cp] == 12)
         {
            f.EdgeShape(cp, 1, "Protoss Dark Archon", 22, 3, 75);
            f.EdgeShape(cp, 1, "40 + 1n Gantrithor", 22, 3, 75);
            f.DotShape(cp, 1, "40 + 1n Gantrithor", 0, 0);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);
         }
         else if (f.loop[cp] == 13)
         {
            f.EdgeShape(cp, 1, "60 + 1n Archon", 45, 3, 100);
            f.EdgeShape(cp, 1, "50 + 1n Battlecruiser", 45, 3, 100);
            f.DotShape(cp, 1, "50 + 1n Battlecruiser", 0, 0);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, "Anywhere");
         }
         else if (f.loop[cp] == 15)
         {
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 20)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }

      else if (f.count[cp] == 7)
      {
         KillUnitAt(All, "60 + 1n Siege", "Anywhere", cp);
         KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", cp);
         KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);

         f.SkillEnd(cp);
      }

   }
}

